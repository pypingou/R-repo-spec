%global packname  dyebias
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          The GASSCO method for correcting for slide-dependent gene-specific dye bias

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-marray R-Biobase 

BuildRequires:    R-devel tex(latex) R-marray R-Biobase 

%description
Many two-colour hybridizations suffer from a dye bias that is both
gene-specific and slide-specific. The former depends on the content of the
nucleotide used for labeling; the latter depends on the labeling
percentage. The slide-dependency was hitherto not recognized, and made
addressing the artefact impossible.  Given a reasonable number of
dye-swapped pairs of hybridizations, or of same vs. same hybridizations,
both the gene- and slide-biases can be estimated and corrected using the
GASSCO method (Margaritis et al., Mol. Sys. Biol. 5:266 (2009),

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora