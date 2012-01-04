%global packname  PoMoS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Polynomial (ordinary differential equation) Model Search

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RGtk2 R-cairoDevice R-igraph 


BuildRequires:    R-devel tex(latex) R-RGtk2 R-cairoDevice R-igraph



%description
PoMoS-package aims to determine from a set of N time series the optimal
polynomial structure of a model built on first-order ordinary differential
equations. The core of the package is based on the poMoS function: an
evolutionary algorithm combined with a least square fitting. Optimality is
estimated with AIC (Akaike, 1974) or AIC-like criterions. Although
efficient in its selection, the identification of the optimal structure
cannot be guaranteed. Therefore, both selected and rejected models are
reconsidered after optimal solutions are obtained from the evolutionary
algorithm for another analysis. This analysis is based on a statistical
evaluation of the regressors' quality.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora