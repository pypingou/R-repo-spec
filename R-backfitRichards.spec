%global packname  backfitRichards
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Backfitted independent values of Richards curves

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-richards R-methods 

BuildRequires:    R-devel tex(latex) R-richards R-methods 

%description
Backfitted independent values of Richards curves are computed and plotted.

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
%doc %{rlibdir}/backfitRichards/html
%doc %{rlibdir}/backfitRichards/DESCRIPTION
%{rlibdir}/backfitRichards/R
%{rlibdir}/backfitRichards/help
%{rlibdir}/backfitRichards/INDEX
%{rlibdir}/backfitRichards/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora