%global packname  hdrcde
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.15
Release:          1%{?dist}
Summary:          Highest density regions and conditional density estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-locfit R-ash R-ks R-KernSmooth 


BuildRequires:    R-devel tex(latex) R-locfit R-ash R-ks R-KernSmooth



%description
Computation of highest density regions in one and two dimensions, kernel
estimation of univariate density functions conditional on one covariate,
and multimodal regression.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.15-1
- initial package for Fedora