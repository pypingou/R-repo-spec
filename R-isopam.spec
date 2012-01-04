%global packname  isopam
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.10
Release:          1%{?dist}
Summary:          Isopam (Clustering)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster R-vegan 


BuildRequires:    R-devel tex(latex) R-cluster R-vegan



%description
Isopam clustering algorithm and utilities. Isopam optimizes clusters and
optionally cluster numbers in a brute force style and aims at an optimum
separation by all or some descriptors (typically species).

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.10-1
- initial package for Fedora