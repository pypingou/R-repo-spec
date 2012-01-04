%global packname  HAPim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          HapIM

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package provides a set of functions whose aim is to propose 4 methods
of QTL detection. HAPimLD is an interval-mapping method designed for
unrelated individuals with no family information that makes use of linkage
disequilibrium. HAPimLDL is an interval-mapping method for design of
half-sib families. It combines linkage analysis and linkage
disequilibrium. HaploMax is based on an analysis of variance with a dose
haplotype effect. HaploMaxHS is based on an analysis of variance with a
sire effect and a dose haplotype effect in half-sib family design. 
Fundings for the package development were provided to the LDLmapQTL
project by the ANR GENANIMAL program and APIS-GENE.

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
%doc %{rlibdir}/HAPim/html
%doc %{rlibdir}/HAPim/DESCRIPTION
%{rlibdir}/HAPim/R
%{rlibdir}/HAPim/Meta
%{rlibdir}/HAPim/data
%{rlibdir}/HAPim/INDEX
%{rlibdir}/HAPim/help
%{rlibdir}/HAPim/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora