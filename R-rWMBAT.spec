%global packname  rWMBAT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          The William and Mary Bayesian Analysis Tool

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains all the functions used to get a resulting Bayesian

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
%doc %{rlibdir}/rWMBAT/doc
%doc %{rlibdir}/rWMBAT/html
%doc %{rlibdir}/rWMBAT/DESCRIPTION
%{rlibdir}/rWMBAT/libs
%{rlibdir}/rWMBAT/data
RPM build errors:
%{rlibdir}/rWMBAT/Meta
%{rlibdir}/rWMBAT/help
%{rlibdir}/rWMBAT/R
%{rlibdir}/rWMBAT/INDEX
%{rlibdir}/rWMBAT/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora