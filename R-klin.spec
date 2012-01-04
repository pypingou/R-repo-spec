%global packname  klin
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2007.02.05
Release:          1%{?dist}
Summary:          Linear equations with Kronecker structure

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2007-02-05.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
The package implements efficient ways to evaluate and solve equations of
the form Ax=b, where A is a kronecker product of matrices.  Functions to
solve least squares problems of this type are also included.

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
%doc %{rlibdir}/klin/DESCRIPTION
%doc %{rlibdir}/klin/html
%{rlibdir}/klin/Meta
%{rlibdir}/klin/INDEX
%{rlibdir}/klin/R
%{rlibdir}/klin/NAMESPACE
%{rlibdir}/klin/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2007.02.05-1
- initial package for Fedora