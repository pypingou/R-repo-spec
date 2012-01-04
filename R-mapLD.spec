%global packname  mapLD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Linkage Disequilibrium Mapping

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
mapLD measures linkage disequilibrium and constructs haplotype blocks
using the method described in Gabriel et al (2002) and Wall & Prichard

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
%doc %{rlibdir}/mapLD/html
%doc %{rlibdir}/mapLD/DESCRIPTION
%{rlibdir}/mapLD/R
%{rlibdir}/mapLD/INDEX
%{rlibdir}/mapLD/data
%{rlibdir}/mapLD/NAMESPACE
%{rlibdir}/mapLD/Meta
%{rlibdir}/mapLD/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora