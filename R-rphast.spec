%global packname  rphast
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          R interface to PHAST software for comparative genomics

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
RPHAST is an R interface to the PHAST pacakge (Phylogenetic Analyis with
Space/Time Models).  It can be used for many types of analysis in
comparative and evolutionary genomics, such as estimating models of
evolution from sequence data, scoring alignments for conservation or
acceleration, and predicting elements based on conservation or custom
phylogenetic hidden Markov models.  It can also perform many basic
operations on multiple sequence alignments and phylogenetic trees.

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
%doc %{rlibdir}/rphast/html
%doc %{rlibdir}/rphast/DESCRIPTION
%doc %{rlibdir}/rphast/doc
%{rlibdir}/rphast/Meta
%{rlibdir}/rphast/libs
%{rlibdir}/rphast/NAMESPACE
%{rlibdir}/rphast/R
%{rlibdir}/rphast/extdata
%{rlibdir}/rphast/INDEX
%{rlibdir}/rphast/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora