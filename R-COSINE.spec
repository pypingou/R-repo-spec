%global packname  COSINE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          COndition SpecIfic sub-NEtwork

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-genalg 

BuildRequires:    R-devel tex(latex) R-MASS R-genalg 

%description
To identify the globally most discriminative subnetwork from gene
expression profiles and protein-protein interactions data using an
optimization method and genetic algorithm

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
%doc %{rlibdir}/COSINE/DESCRIPTION
%doc %{rlibdir}/COSINE/html
%{rlibdir}/COSINE/R
%{rlibdir}/COSINE/Meta
%{rlibdir}/COSINE/INDEX
%{rlibdir}/COSINE/data
%{rlibdir}/COSINE/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora