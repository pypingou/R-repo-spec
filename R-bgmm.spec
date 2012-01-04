%global packname  bgmm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Gaussian Mixture Modeling algorithms. Including the belief-based mixture modeling.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm R-car R-lattice R-combinat 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-car R-lattice R-combinat 

%description


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
%doc %{rlibdir}/bgmm/html
%doc %{rlibdir}/bgmm/DESCRIPTION
%doc %{rlibdir}/bgmm/CITATION
%{rlibdir}/bgmm/INDEX
%{rlibdir}/bgmm/Meta
%{rlibdir}/bgmm/NAMESPACE
%{rlibdir}/bgmm/R
%{rlibdir}/bgmm/data
%{rlibdir}/bgmm/demo
%{rlibdir}/bgmm/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora