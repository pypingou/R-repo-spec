%global packname  eqtl
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Tools for analyzing eQTL experiments: A complementary to Karl Broman's 'qtl' package for genome-wide analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-qtl 


BuildRequires:    R-devel tex(latex) R-qtl



%description
Analysis of experimental crosses to identify genes (called quantitative
trait loci, QTLs) contributing to variation in quantitative traits.

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
%doc %{rlibdir}/eqtl/html
%doc %{rlibdir}/eqtl/DESCRIPTION
%{rlibdir}/eqtl/data
%{rlibdir}/eqtl/NAMESPACE
%{rlibdir}/eqtl/help
%{rlibdir}/eqtl/Meta
%{rlibdir}/eqtl/R
%{rlibdir}/eqtl/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora