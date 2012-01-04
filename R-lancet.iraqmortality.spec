%global packname  lancet.iraqmortality
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Surveys of Iraq Mortality Published in The Lancet

Group:            Applications/Engineering 
License:          GPL version 2 or later.
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreign 

BuildRequires:    R-devel tex(latex) R-foreign 

%description
The Lancet has published two surveys (Roberts et al (2004) and Burnham et
al (2006)) on Iraq mortality before and after the US-led invasion. This
package serves three purposes. First, it includes a portion of the summary
data related to the first study, both the raw .xls file distributed by the
authors and a cleaned up R dataframe. Second, it provides simple functions
for working with data from the second study. The authors have distributed
this data only to selected researchers. Those researchers can use this
package to work with that data more easily. Third, for researchers without
such access, we provide a vignette which serves as a guided tour of some
of the more interesting aspects of the data.

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
%doc %{rlibdir}/lancet.iraqmortality/doc
%doc %{rlibdir}/lancet.iraqmortality/DESCRIPTION
%doc %{rlibdir}/lancet.iraqmortality/html
%{rlibdir}/lancet.iraqmortality/doc_rnw
%{rlibdir}/lancet.iraqmortality/help
%{rlibdir}/lancet.iraqmortality/INDEX
%{rlibdir}/lancet.iraqmortality/Meta
%{rlibdir}/lancet.iraqmortality/NAMESPACE
RPM build errors:
%{rlibdir}/lancet.iraqmortality/R
%{rlibdir}/lancet.iraqmortality/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora