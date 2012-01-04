%global packname  IsoGene
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.19
Release:          1%{?dist}
Summary:          Testing for monotonic relationship between gene expression and doses in a microarray experiment.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-19.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-xtable R-Iso R-affy R-ff 


BuildRequires:    R-devel tex(latex) R-tcltk R-xtable R-Iso R-affy R-ff



%description
Several testing procedures including the global likelihood ratio test
(Bartholomew, 1961), Williams (1971, 1972), Marcus (1976), M (Hu et al.
2005) and the modified M (Lin et al. 2007) are used to test for the
monotonic trend in gene expression with respect to doses. BH (Benjamini
and Hochberg 1995) and BY (Benjamini and Yekutilie 2004) FDR controlling
procedures are applied to adjust the raw p-values obtained from the

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.19-1
- initial package for Fedora