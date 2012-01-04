%global packname  jointDiag
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Joint Approximate Diagonalization of a set of square matrices

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Different algorithms to perform approximate joint diagonalization of a
finite set of square matrices. Depending on the algorithm, orthogonal or
non-orthogonal diagonalizer is found. These algorithms are particularly
useful in the context of blind source separation.

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
%doc %{rlibdir}/jointDiag/html
%doc %{rlibdir}/jointDiag/DESCRIPTION
%{rlibdir}/jointDiag/R
%{rlibdir}/jointDiag/help
%{rlibdir}/jointDiag/NAMESPACE
%{rlibdir}/jointDiag/INDEX
%{rlibdir}/jointDiag/Meta
%{rlibdir}/jointDiag/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora