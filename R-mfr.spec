%global packname  mfr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.00.00
Release:          1%{?dist}
Summary:          Minimal Free Resolutions of Graph Edge Ideals

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Algebraic Geometry: Minimal Free Resolutions of the Edge Ideal of a Graph

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
%doc %{rlibdir}/mfr/html
%doc %{rlibdir}/mfr/DESCRIPTION
%{rlibdir}/mfr/libs
%{rlibdir}/mfr/Meta
%{rlibdir}/mfr/NAMESPACE
%{rlibdir}/mfr/INDEX
%{rlibdir}/mfr/R
%{rlibdir}/mfr/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.00.00-1
- initial package for Fedora