%global packname  howmany
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          A lower bound for the number of correct rejections

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
When testing multiple hypotheses simultaneously, this package provides
functionality to calculate a lower bound for the number of correct
rejections (as a function of the number of rejected hypotheses), which
holds simultaneously -with high probability- for all possible number of
rejections. As a special case, a lower bound for the total number of false
null hypotheses can be inferred. Dependent test statistics can be handled
for multiple tests of associations. For independent test statistics, it is
sufficient to provide a list of p-values.

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
%doc %{rlibdir}/howmany/html
%doc %{rlibdir}/howmany/DESCRIPTION
%{rlibdir}/howmany/help
%{rlibdir}/howmany/Meta
%{rlibdir}/howmany/R
%{rlibdir}/howmany/INDEX
%{rlibdir}/howmany/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora