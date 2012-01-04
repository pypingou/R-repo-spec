%global packname  emdbook
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Ecological models and data (book support)

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-lattice 

BuildRequires:    R-devel tex(latex) R-MASS R-lattice 

%description
Auxiliary functions and data sets for _Ecological Models and Data_, a book
presenting maximum likelihood estimation and related topics for ecologists
(ISBN 978-0-691-12522-0)

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
%doc %{rlibdir}/emdbook/html
%doc %{rlibdir}/emdbook/DESCRIPTION
%doc %{rlibdir}/emdbook/doc
%doc %{rlibdir}/emdbook/CITATION
%{rlibdir}/emdbook/BUGS
%{rlibdir}/emdbook/help
%{rlibdir}/emdbook/Meta
%{rlibdir}/emdbook/R
%{rlibdir}/emdbook/data
%{rlibdir}/emdbook/INDEX
%{rlibdir}/emdbook/misc
%{rlibdir}/emdbook/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora