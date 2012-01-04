%global packname  mefa4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Multivariate Data Handling with S4 Classes and Sparse Matrices

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Matrix 

BuildRequires:    R-devel tex(latex) R-methods R-Matrix 

%description
An S4 update of the 'mefa' package using sparse matrices for enhanced
efficiency.  Sparse array-like obejects are supported via lists of sparse

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
%doc %{rlibdir}/mefa4/CITATION
%doc %{rlibdir}/mefa4/COPYING
%doc %{rlibdir}/mefa4/html
%doc %{rlibdir}/mefa4/DESCRIPTION
%doc %{rlibdir}/mefa4/doc
%{rlibdir}/mefa4/help
%{rlibdir}/mefa4/INDEX
%{rlibdir}/mefa4/Meta
%{rlibdir}/mefa4/NAMESPACE
RPM build errors:
%{rlibdir}/mefa4/ChangeLog
%{rlibdir}/mefa4/R
%{rlibdir}/mefa4/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora