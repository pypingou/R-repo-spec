%global packname  MFSAS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Creation and Evaluation of Multilevel Fixed and Sequential Sampling Plans

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
This package provides functionality for creating and evaluating acceptance
sampling plans for attributes when there are k (>=2) levels of product
quality. Plans can be multilevel fixed, or multilevel sequential.

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
%doc %{rlibdir}/MFSAS/CITATION
%doc %{rlibdir}/MFSAS/doc
%doc %{rlibdir}/MFSAS/DESCRIPTION
%doc %{rlibdir}/MFSAS/html
%{rlibdir}/MFSAS/INDEX
%{rlibdir}/MFSAS/NAMESPACE
%{rlibdir}/MFSAS/help
%{rlibdir}/MFSAS/R
%{rlibdir}/MFSAS/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora