%global packname  IsoGeneGUI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          A graphical user interface to conduct a dose-response analysis of microarray data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tkrplot R-IsoGene 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot R-IsoGene 

%description
The IsoGene Graphical User Interface (IsoGene-GUI) is a user friendly
interface of the IsoGene package which is aimed to identify for genes with
a monotonic trend in the expression levels with respect to the increasing
doses using several test statistics: global likelihood ratio test (E2),
Bartholomew 1961, Barlow et al. 1972 and Robertson et al. 1988), Williams
(1971, 1972), Marcus (1976), the M (Hu et al. 2005) and the modified M
(Lin et al. 2007).  The p-values of the global likelihood ratio test (E2)
are obtained using the excat distribution and permutation. The other four
test statistics are obtained using permutation . Several p-values
adjustment are provided:  Bonferroni, Holm (1979), Hochberg (1988), and
Sidak procedures for controlling the family-wise Type I error rate (FWER),
and BH (Benjamini and Hochberg 1995) and BY (Benjamini and Yekutieli 2001)
procedures are used for controlling the FDR. the inference is based on
resampling methods, which control the False Discovery Rate (FDR) (both
permutations (Ge et al., 2003) and the Significance Analysis of
Microarrays (SAM), Tusher et al., 2001).

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora