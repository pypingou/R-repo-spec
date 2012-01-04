%global packname  ResourceSelection
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Resource Selection (Probability) Functions for Use-Availability Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Resource Selection (Probability) Functions for use-availability wildlife
data as described in Lele and Keim (2006, Ecology 87, 3021--3028), and
Lele (2009, J. Wildlife Management 73, 122--127).

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
%doc %{rlibdir}/ResourceSelection/COPYING
%doc %{rlibdir}/ResourceSelection/html
%doc %{rlibdir}/ResourceSelection/DESCRIPTION
%{rlibdir}/ResourceSelection/NAMESPACE
%{rlibdir}/ResourceSelection/Meta
%{rlibdir}/ResourceSelection/ChangeLog
%{rlibdir}/ResourceSelection/R
%{rlibdir}/ResourceSelection/INDEX
%{rlibdir}/ResourceSelection/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora