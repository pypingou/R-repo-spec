%global packname  SparseM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.89
Release:          1%{?dist}
Summary:          Sparse Linear Algebra

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-utils 

%description
Basic linear algebra for sparse matrices

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
%doc %{rlibdir}/SparseM/html
%doc %{rlibdir}/SparseM/DESCRIPTION
%doc %{rlibdir}/SparseM/doc
%{rlibdir}/SparseM/libs
%{rlibdir}/SparseM/INDEX
%{rlibdir}/SparseM/data
%{rlibdir}/SparseM/Meta
%{rlibdir}/SparseM/ChangeLog
%{rlibdir}/SparseM/R
%{rlibdir}/SparseM/NAMESPACE
%{rlibdir}/SparseM/demo
%{rlibdir}/SparseM/LICENSE
%{rlibdir}/SparseM/help
%{rlibdir}/SparseM/extdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.89-1
- initial package for Fedora