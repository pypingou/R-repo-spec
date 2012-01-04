%global packname  ldbounds
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Lan-DeMets Method for Group Sequential Boundaries

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Computations related to group sequential boundaries. Includes calculation
of bounds using the Lan-DeMets alpha spending function approach.

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
%doc %{rlibdir}/ldbounds/html
%doc %{rlibdir}/ldbounds/doc
%doc %{rlibdir}/ldbounds/DESCRIPTION
%{rlibdir}/ldbounds/Meta
%{rlibdir}/ldbounds/INDEX
%{rlibdir}/ldbounds/R
%{rlibdir}/ldbounds/NAMESPACE
%{rlibdir}/ldbounds/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora