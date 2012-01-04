%global packname  maqcExpression4plex
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Sample Expression Data - MAQC / HG18 - NimbleGen

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data from human (HG18) 4plex NimbleGen array. It has 24k genes with 3
60mer probes per gene.

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
%doc %{rlibdir}/maqcExpression4plex/DESCRIPTION
%doc %{rlibdir}/maqcExpression4plex/html
%{rlibdir}/maqcExpression4plex/help
%{rlibdir}/maqcExpression4plex/extdata
%{rlibdir}/maqcExpression4plex/INDEX
%{rlibdir}/maqcExpression4plex/R
%{rlibdir}/maqcExpression4plex/Meta
%{rlibdir}/maqcExpression4plex/NAMESPACE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora