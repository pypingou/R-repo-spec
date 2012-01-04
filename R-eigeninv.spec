%global packname  eigeninv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2011.8.1
Release:          1%{?dist}
Summary:          Generates (dense) matrices that have a given set of eigenvalues

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Solves the ``inverse eigenvalue problem'' which is to generate a
real-valued matrix that has the specified real eigenvalue spectrum.  It
can generate infinitely many dense matrices, symmetric or asymmetric, with
the given set of eigenvalues.  Algorithm can also generate stochastic and
doubly stochastic matrices.

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
%doc %{rlibdir}/eigeninv/DESCRIPTION
%doc %{rlibdir}/eigeninv/html
%doc %{rlibdir}/eigeninv/NEWS
%{rlibdir}/eigeninv/INDEX
%{rlibdir}/eigeninv/R
%{rlibdir}/eigeninv/demo
%{rlibdir}/eigeninv/NAMESPACE
%{rlibdir}/eigeninv/Meta
%{rlibdir}/eigeninv/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.8.1-1
- initial package for Fedora