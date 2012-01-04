%global packname  seacarb
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.4.3
Release:          1%{?dist}
Summary:          seawater carbonate chemistry with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Calculates parameters of the seawater carbonate system. Code and/or
corrections were contributed by Andreas Andersson, Jean-Marie Epitalon,
Bernard Gentili, Andreas Hofmann, Jim Orr, Aurelien Proye and Karline

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
%doc %{rlibdir}/seacarb/DESCRIPTION
%doc %{rlibdir}/seacarb/html
%{rlibdir}/seacarb/Meta
%{rlibdir}/seacarb/R
%{rlibdir}/seacarb/data
%{rlibdir}/seacarb/help
%{rlibdir}/seacarb/NAMESPACE
%{rlibdir}/seacarb/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.3-1
- initial package for Fedora