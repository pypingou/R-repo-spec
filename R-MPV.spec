%global packname  MPV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.25
Release:          1%{?dist}
Summary:          Data Sets from Montgomery, Peck and Vining's Book

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
These data sets are taken from the book Introduction to Linear Regression
Analysis (3rd ed), by the above authors.

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
%doc %{rlibdir}/MPV/DESCRIPTION
%doc %{rlibdir}/MPV/html
%{rlibdir}/MPV/R
%{rlibdir}/MPV/Meta
%{rlibdir}/MPV/NAMESPACE
%{rlibdir}/MPV/help
%{rlibdir}/MPV/data
%{rlibdir}/MPV/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.25-1
- initial package for Fedora