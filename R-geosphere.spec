%global packname  geosphere
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.26
Release:          1%{?dist}
Summary:          Spherical Trigonometry

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-26.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Spherical trigonometry for geographic applications

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
%doc %{rlibdir}/geosphere/doc
%doc %{rlibdir}/geosphere/DESCRIPTION
%doc %{rlibdir}/geosphere/html
%{rlibdir}/geosphere/NAMESPACE
%{rlibdir}/geosphere/Meta
%{rlibdir}/geosphere/INDEX
%{rlibdir}/geosphere/data
%{rlibdir}/geosphere/R
%{rlibdir}/geosphere/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.26-1
- initial package for Fedora