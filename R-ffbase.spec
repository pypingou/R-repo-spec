%global packname  ffbase
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Basic statistical functions for package ff

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ff 

BuildRequires:    R-devel tex(latex) R-ff 

%description
Implementation for min,max, mean, tabulate, table, with, within. for
package ff

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
%doc %{rlibdir}/ffbase/DESCRIPTION
%doc %{rlibdir}/ffbase/html
%doc %{rlibdir}/ffbase/NEWS
%{rlibdir}/ffbase/help
%{rlibdir}/ffbase/Meta
%{rlibdir}/ffbase/INDEX
%{rlibdir}/ffbase/tests
%{rlibdir}/ffbase/R
%{rlibdir}/ffbase/NAMESPACE

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.1-1
- initial package for Fedora