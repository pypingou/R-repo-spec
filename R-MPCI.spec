%global packname  MPCI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Multivariate Process Capability Indices (MPCI)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
MPCI package performs the followings Multivariate Process Capability
Indices: Shahriari et al. (1995) Multivariate Capability Vector, Taam et
al. (1993) Multivariate Capability Index (MCpm) and the followings based
on Principal Componenet Analysis (PCA):Wang and Chen (1998), Xekalaki and
Perakis (2002) and Wang (2005). Moreover, include two datasets.

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
%doc %{rlibdir}/MPCI/html
%doc %{rlibdir}/MPCI/DESCRIPTION
%{rlibdir}/MPCI/Meta
%{rlibdir}/MPCI/NAMESPACE
%{rlibdir}/MPCI/R
%{rlibdir}/MPCI/data
%{rlibdir}/MPCI/help
%{rlibdir}/MPCI/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora