%global packname  reliaR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.01
Release:          1%{?dist}
Summary:          Package for some probability distributions.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of utilities for some reliability models/probability

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
%doc %{rlibdir}/reliaR/doc
%doc %{rlibdir}/reliaR/DESCRIPTION
%doc %{rlibdir}/reliaR/html
%{rlibdir}/reliaR/Meta
%{rlibdir}/reliaR/NAMESPACE
RPM build errors:
%{rlibdir}/reliaR/data
%{rlibdir}/reliaR/help
%{rlibdir}/reliaR/R
%{rlibdir}/reliaR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.01-1
- initial package for Fedora