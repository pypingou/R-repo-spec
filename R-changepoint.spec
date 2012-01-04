%global packname  changepoint
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          An R package for changepoint analysis

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-base 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-base 

%description
Implements various mainstream and specialised changepoint methods for
finding single and multiple changepoints within data.  Many popular
non-parametric and frequentist methods are included.  The cpt.mean,
cpt.var, cpt.meanvar functions should be your first point of call.

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
%doc %{rlibdir}/changepoint/NEWS
%doc %{rlibdir}/changepoint/html
%doc %{rlibdir}/changepoint/DESCRIPTION
%{rlibdir}/changepoint/data
%{rlibdir}/changepoint/R
%{rlibdir}/changepoint/NAMESPACE
%{rlibdir}/changepoint/help
%{rlibdir}/changepoint/INDEX
%{rlibdir}/changepoint/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora