%global packname  kinship
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          mixed-effects Cox models, sparse matrices, and modeling data from large pedigrees

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-survival R-nlme R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-survival R-nlme R-lattice 

%description
coxme: general mixed-effects Cox models; kinship: routines to create and
manipulate n by n matrices that describe the genetic relationships between
n persons; pedigree: create and plot pedigrees; bdsmatrix: a class of
objects for sparse block-diagonal matrices (which is how kinship matrices
are stored); gchol: generalized cholesky decompositions

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
%doc %{rlibdir}/kinship/html
%doc %{rlibdir}/kinship/DESCRIPTION
%doc %{rlibdir}/kinship/doc
%{rlibdir}/kinship/libs
%{rlibdir}/kinship/help
%{rlibdir}/kinship/tests
%{rlibdir}/kinship/Meta
%{rlibdir}/kinship/INDEX
%{rlibdir}/kinship/R
RPM build errors:
%{rlibdir}/kinship/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora