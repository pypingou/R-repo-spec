%global packname  cherry
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Multiple testing methods for exploratory research

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-bitops 

BuildRequires:    R-devel tex(latex) R-methods R-bitops 

%description
This package implements a class of multiple testing methods that does not
prescribe the user what hypotheses to reject, but instead allows the user
to select the set of selected hypotheses freely. The multiple testing
procedure aids this selection by providing an upper confidence bound for
the number of false rejections among the selected set. Because the
confidence bounds are simultaneous for all possible rejected sets, the
validity is not compromised by post hoc selection.

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
%doc %{rlibdir}/cherry/html
%doc %{rlibdir}/cherry/DESCRIPTION
%{rlibdir}/cherry/help
%{rlibdir}/cherry/R
%{rlibdir}/cherry/INDEX
%{rlibdir}/cherry/NAMESPACE
%{rlibdir}/cherry/data
%{rlibdir}/cherry/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora