%global packname  itertools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Iterator Tools

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-iterators 

BuildRequires:    R-devel tex(latex) R-iterators 

%description
Various tools for creating iterators, many patterned after functions in
the Python itertools module, and others patterned after functions in the
'snow' package.

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
%doc %{rlibdir}/itertools/NEWS
%doc %{rlibdir}/itertools/html
%doc %{rlibdir}/itertools/DESCRIPTION
%{rlibdir}/itertools/Meta
%{rlibdir}/itertools/examples
%{rlibdir}/itertools/INDEX
%{rlibdir}/itertools/NAMESPACE
%{rlibdir}/itertools/help
%{rlibdir}/itertools/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora