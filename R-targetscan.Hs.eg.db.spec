%global packname  targetscan.Hs.eg.db
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          TargetScan miRNA target predictions for human

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-AnnotationDbi 
Requires:         R-methods R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-methods R-AnnotationDbi
BuildRequires:    R-methods R-AnnotationDbi 


%description
TargetScan miRNA target predictions for human assembled using data from
the TargetScan website. TargetScan predicts biological targets of miRNAs
by searching for the presence of conserved 8mer and 7mer sites that match
the seed region of each miRNA. Also identified are sites with mismatches
in the seed region that are compensated by conserved 3' pairing. In
mammals, predictions are ranked based on the predicted efficacy of
targeting as calculated using the context scores of the sites.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora