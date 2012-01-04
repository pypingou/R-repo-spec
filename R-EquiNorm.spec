%global packname  EquiNorm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Normalize expression data using equivalently expressed genes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-lattice 
Requires:         R-lme4 R-mvtnorm R-lemma 

BuildRequires:    R-devel tex(latex) R-Matrix R-lattice
BuildRequires:    R-lme4 R-mvtnorm R-lemma 


%description
Normalize oligonucleotide gene expression data using equivalently
expressed genes in experiments comparing two groups of samples (for
example, case-control samples), as outlined in L-X Qin and JM Satagopan

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
%doc %{rlibdir}/EquiNorm/html
%doc %{rlibdir}/EquiNorm/DESCRIPTION
%{rlibdir}/EquiNorm/R
%{rlibdir}/EquiNorm/Meta
%{rlibdir}/EquiNorm/NAMESPACE
%{rlibdir}/EquiNorm/help
%{rlibdir}/EquiNorm/INDEX
%{rlibdir}/EquiNorm/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora