%global packname  tabplot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11
Release:          1%{?dist}
Summary:          Tableplot, a visualization of large datasets

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-data.table R-grid 

BuildRequires:    R-devel tex(latex) R-data.table R-grid 

%description
A tableplot is a visualisation of a (large) dataset with a dozen of
variables, both numeric and categorical. Each column represents a variable
and each row bin is an aggregate of a certain number of records.  Numeric
variables are visualized as bar charts, and categorical variables as
stacked bar charts. Missing values are taken into account. Also supports
large ffdf datasets from the ff package.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/tabplot/html
%doc %{rlibdir}/tabplot/DESCRIPTION
%doc %{rlibdir}/tabplot/doc
%{rlibdir}/tabplot/help
%{rlibdir}/tabplot/tests
%{rlibdir}/tabplot/demo
%{rlibdir}/tabplot/NAMESPACE
%{rlibdir}/tabplot/Meta
%{rlibdir}/tabplot/INDEX
%{rlibdir}/tabplot/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11-1
- initial package for Fedora