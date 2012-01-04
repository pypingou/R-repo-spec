%global packname  ffmanova
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1.2
Release:          1%{?dist}
Summary:          Fifty-fifty MANOVA

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package performs general linear modeling with multiple responses
(MANCOVA).  An overall p-value for each model term is calculated by the
50-50 MANOVA method, which handles collinear responses.  Rotation testing
is used to compute adjusted single response p-values according to
familywise error rates and false discovery rates.

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
%doc %{rlibdir}/ffmanova/html
%doc %{rlibdir}/ffmanova/DESCRIPTION
%{rlibdir}/ffmanova/INDEX
%{rlibdir}/ffmanova/R
%{rlibdir}/ffmanova/NAMESPACE
%{rlibdir}/ffmanova/data
%{rlibdir}/ffmanova/Meta
%{rlibdir}/ffmanova/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1.2-1
- initial package for Fedora