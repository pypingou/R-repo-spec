%global packname  ks
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.4
Release:          1%{?dist}
Summary:          Kernel smoothing

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-KernSmooth R-mvtnorm R-rgl R-misc3d 


BuildRequires:    R-devel tex(latex) R-stats R-KernSmooth R-mvtnorm R-rgl R-misc3d



%description
Kernel smoothers for univariate and multivariate data

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.4-1
- initial package for Fedora