%global packname  ipptoolbox
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          IPP Toolbox

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-AlgDesign R-copula R-evd R-triangle 

BuildRequires:    R-devel tex(latex) R-AlgDesign R-copula R-evd R-triangle 

%description
An R package for uncertainty quantification and propagation in the
framework of Dempster-Shafer Theory and imprecise probabilities. This
package was developed in the context of a collaborative research project
between EDF R&D (http//rd.edf.com) and the University of Duisburg-Essen,
Information Logistics (http//www.uni-due.de/il).

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
%doc %{rlibdir}/ipptoolbox/DESCRIPTION
%doc %{rlibdir}/ipptoolbox/html
%{rlibdir}/ipptoolbox/NAMESPACE
%{rlibdir}/ipptoolbox/R
%{rlibdir}/ipptoolbox/Meta
%{rlibdir}/ipptoolbox/INDEX
%{rlibdir}/ipptoolbox/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora