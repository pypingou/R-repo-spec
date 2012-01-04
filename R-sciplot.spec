%global packname  sciplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Scientific Graphing Functions for Factorial Designs

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
A collection of functions that creates graphs with error bars for data
collected from one-way or higher factorial designs.

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
%doc %{rlibdir}/sciplot/DESCRIPTION
%doc %{rlibdir}/sciplot/html
%{rlibdir}/sciplot/R
%{rlibdir}/sciplot/NAMESPACE
%{rlibdir}/sciplot/help
%{rlibdir}/sciplot/INDEX
%{rlibdir}/sciplot/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9-1
- initial package for Fedora