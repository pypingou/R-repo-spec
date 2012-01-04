%global packname  pd.hg18.60mer.expr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.8.0
Release:          1%{?dist}
Summary:          Platform Design Info for NimbleGen hg18_60mer_expr

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-RSQLite R-oligoClasses R-DBI 


BuildRequires:    R-devel tex(latex) R-methods R-RSQLite R-oligoClasses R-DBI



%description
Platform Design Info for NimbleGen hg18_60mer_expr

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
%doc %{rlibdir}/pd.hg18.60mer.expr/DESCRIPTION
%doc %{rlibdir}/pd.hg18.60mer.expr/html
%{rlibdir}/pd.hg18.60mer.expr/extdata
%{rlibdir}/pd.hg18.60mer.expr/Meta
%{rlibdir}/pd.hg18.60mer.expr/UnitTests
%{rlibdir}/pd.hg18.60mer.expr/help
%{rlibdir}/pd.hg18.60mer.expr/data
%{rlibdir}/pd.hg18.60mer.expr/R
%{rlibdir}/pd.hg18.60mer.expr/NAMESPACE
%{rlibdir}/pd.hg18.60mer.expr/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.8.0-1
- initial package for Fedora