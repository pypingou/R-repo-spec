%global packname  paramlink
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Parametric linkage analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-kinship 


BuildRequires:    R-devel tex(latex) R-kinship



%description
Parametric pedigree analysis based on the Elston-Stewart algorithm.
Singlepoint LOD scores and power analysis for diallelic markers. Also
includes functions for manipulating and plotting pedigrees and linkage

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
%doc %{rlibdir}/paramlink/html
%doc %{rlibdir}/paramlink/DESCRIPTION
%{rlibdir}/paramlink/NAMESPACE
%{rlibdir}/paramlink/data
%{rlibdir}/paramlink/Meta
%{rlibdir}/paramlink/R
%{rlibdir}/paramlink/INDEX
%{rlibdir}/paramlink/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora