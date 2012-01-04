%global packname  snm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Supervised Normalization of Microarrays

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lme4 R-splines R-corpcor 


BuildRequires:    R-devel tex(latex) R-lme4 R-splines R-corpcor



%description
SNM is a modeling strategy especially designed for normalizing
high-throughput genomic data. The underlying premise of our approach is
that your data is a function of what we refer to as study-specific
variables. These variables are either biological variables that represent
the target of the statistical analysis, or adjustment variables that
represent factors arising from the experimental or biological setting the
data is drawn from. The SNM approach aims to simultaneously model all
study-specific variables in order to more accurately characterize the
biological or clinical variables of interest.

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
%doc %{rlibdir}/snm/DESCRIPTION
%doc %{rlibdir}/snm/doc
%doc %{rlibdir}/snm/html
%doc %{rlibdir}/snm/NEWS
%{rlibdir}/snm/NAMESPACE
%{rlibdir}/snm/INDEX
%{rlibdir}/snm/Meta
%{rlibdir}/snm/help
%{rlibdir}/snm/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora