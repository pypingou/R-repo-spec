%global packname  sisus
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.09.011
Release:          1%{?dist}
Summary:          SISUS: Stable Isotope Sourcing using Sampling

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.09-011.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-annotate R-ash R-Biobase R-coda R-ellipse R-gclus R-gdata R-geneplotter R-gplots R-gtools R-hdrcde R-moments R-mvtnorm R-polyapost R-rcdd R-RColorBrewer R-stats R-sm 

BuildRequires:    R-devel tex(latex) R-annotate R-ash R-Biobase R-coda R-ellipse R-gclus R-gdata R-geneplotter R-gplots R-gtools R-hdrcde R-moments R-mvtnorm R-polyapost R-rcdd R-RColorBrewer R-stats R-sm 

%description
SISUS for source partitioning using stable isotopes.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.09.011-1
- initial package for Fedora