%global packname  mapproj
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.8.3
Release:          1%{?dist}
Summary:          Map Projections

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-8.3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-maps 

BuildRequires:    R-devel tex(latex) R-maps 

%description
Converts latitude/longitude into projected coordinates.

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
%doc %{rlibdir}/mapproj/html
%doc %{rlibdir}/mapproj/DESCRIPTION
%{rlibdir}/mapproj/LICENSE
%{rlibdir}/mapproj/help
%{rlibdir}/mapproj/NAMESPACE
%{rlibdir}/mapproj/Meta
%{rlibdir}/mapproj/R
%{rlibdir}/mapproj/libs
%{rlibdir}/mapproj/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8.3-1
- initial package for Fedora