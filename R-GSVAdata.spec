%global packname  GSVAdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.3
Release:          1%{?dist}
Summary:          Data employed in the vignette of the GSVA package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase R-GSEABase R-hgu95a.db 

BuildRequires:    R-devel tex(latex) R-Biobase R-GSEABase R-hgu95a.db 

%description
This package stores the data employed in the vignette of the GSVA package.
These data belong to the following publications: Armstrong et al. Nat
Genet 30:41-47, 2002; Verhaak et al. Cancer Cell 17:98-110, 2010; Cahoy et
al. J Neurosci 28:264-278, 2008.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.3-1
- initial package for Fedora