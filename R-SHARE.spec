%global packname  SHARE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          SNP-Haplotype Adaptive REgression (SHARE)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-haplo.stats R-MASS R-methods 

BuildRequires:    R-devel tex(latex) R-haplo.stats R-MASS R-methods 

%description
An adaptive algorithm to select the most informative set of SNPs for
genetic association

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
%doc %{rlibdir}/SHARE/html
%doc %{rlibdir}/SHARE/DESCRIPTION
%doc %{rlibdir}/SHARE/doc
%{rlibdir}/SHARE/NAMESPACE
%{rlibdir}/SHARE/INDEX
%{rlibdir}/SHARE/extdata
%{rlibdir}/SHARE/help
%{rlibdir}/SHARE/Meta
%{rlibdir}/SHARE/data
%{rlibdir}/SHARE/R
%{rlibdir}/SHARE/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora