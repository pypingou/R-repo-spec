%global packname  RPA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          RPA: Robust Probabilistic Averaging for probe-level analysis

Group:            Applications/Engineering 
License:          FreeBSD
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-affydata R-methods 


BuildRequires:    R-devel tex(latex) R-affy R-affydata R-methods



%description
Probabilistic analysis of probe reliability and differential gene
expression on short oligonucleotide arrays. Lahti et al. "Probabilistic
Analysis of Probe Reliability in Differential Gene Expression Studies with
Short Oligonucleotide Arrays", TCBB/IEEE, 2011.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora