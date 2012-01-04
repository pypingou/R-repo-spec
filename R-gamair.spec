%global packname  gamair
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Data for "GAMs: An Introduction with R"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data sets and scripts used in the book "Generalized Additive Models: An
Introduction with R", Wood (2006) CRC.

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
%doc %{rlibdir}/gamair/html
%doc %{rlibdir}/gamair/CITATION
%doc %{rlibdir}/gamair/DESCRIPTION
%{rlibdir}/gamair/help
%{rlibdir}/gamair/INDEX
%{rlibdir}/gamair/NAMESPACE
%{rlibdir}/gamair/scripts
%{rlibdir}/gamair/data
%{rlibdir}/gamair/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7-1
- initial package for Fedora