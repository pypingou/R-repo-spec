%global packname  kzs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Kolmogorov-Zurbenko Spatial Smoothing and Applications

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-lattice R-stats 

BuildRequires:    R-devel tex(latex) R-graphics R-lattice R-stats 

%description
A spatial smoothing algorithm based on convolutions of finite rectangular
kernels that provides sharp resolution in the presence of high levels of

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
%doc %{rlibdir}/kzs/html
%doc %{rlibdir}/kzs/DESCRIPTION
%{rlibdir}/kzs/help
%{rlibdir}/kzs/INDEX
%{rlibdir}/kzs/Meta
%{rlibdir}/kzs/data
%{rlibdir}/kzs/R
%{rlibdir}/kzs/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora